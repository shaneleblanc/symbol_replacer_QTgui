import sys, os, datetime
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl


class Backend(QObject):
    starting_dir_changed = Signal(str)
    chars_to_replace_changed = Signal(str)
    char_to_replace_with_changed = Signal(str)
    log_file_location_changed = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        self.starting_dir_text = ""
        self.chars_to_replace_list = []
        self.char_to_replace_with_text = ""
        self.log_file_location_text = ""
        self.log_file_location = ""
        self.log_file = ""

    @Property(str, notify=starting_dir_changed)
    def starting_dir(self):
        return self.starting_dir_text

    @starting_dir.setter
    def set_starting_dir(self, text):
        if self.starting_dir_text == text:
            return
        self.starting_dir_text = text
        self.starting_dir_changed.emit(self.starting_dir_text)

    @Property(str, notify=chars_to_replace_changed)
    def chars_to_replace(self):
        return self.chars_to_replace_list

    @chars_to_replace.setter
    def set_chars_to_replace(self, text):
        if self.chars_to_replace_list == list(text):
            return
        self.chars_to_replace_list = list(text)
        self.chars_to_replace_changed.emit(self.chars_to_replace_list)

    @Property(str, notify=char_to_replace_with_changed)
    def char_to_replace_with(self):
        return self.char_to_replace_with_text

    @char_to_replace_with.setter
    def set_char_to_replace_with(self, text):
        if self.char_to_replace_with_text == text:
            return
        self.char_to_replace_with_text = text
        self.char_to_replace_with_changed.emit(self.char_to_replace_with_text)

    @Property(str, notify=log_file_location_changed)
    def log_file_location(self):
        return self.log_file_location_text

    @log_file_location.setter
    def set_log_file_location(self, text):
        if self.log_file_location_text == text:
            return
        self.log_file_location_text = text
        self.log_file_location_changed.emit(self.log_file_location_text)

    def validate_fields():
        # Check that starting directory exists and is readable
        if not os.path.exists(self.starting_dir_text):
            # Open Error Dialog "Starting directory does not exist"
            print("Starting directory does not exist.")
        if not os.access(os.path.dirname(self.starting_dir_text), os.R_OK):
            # Open Error Dialog "Starting directory is not readable."
            print("Starting directory is not readable.")
        # Check that log file path exists and is writable, then create it.
        log_file_path = self.log_file_location

        if not (os.path.exists(log_file_path)):
            # Open Error Dialog "Log file path does not exist."
            print("Log file path does not exist.")
        if not os.access(os.path.dirname(log_file_path), os.W_OK):
            # Open Error Dialog "Log file directory is not writable."
            print("Log file directory is not writable.")
        else:
            # Create the file.
            date = datetime.datetime.now()
            date_slug = date.strftime("%m-%d-%y_%H-%M-%S")
            log_file_name = "Renamer_Log_" + date_slug
            self.log_file_locatioon = log_file_path + os.seperator + log_file_name
            open(self.log_file_location, "a")
        # Check that chars_to_replace list is a valid list

        # Check that char_to_replace_with is length 1 and valid OS file name character

    def add_to_queue(self, starting_dir, queue, log, depth='--'):
        for entry in os.scandir(starting_dir):
            if entry.is_dir():
                print('entry is dir: ' + depth + entry.path)
                queue.append(entry.path)
                log.write(depth + ' ' + entry.name + '\n')
                self.add_to_queue(entry.path, queue, log, (depth + '--'))
            elif entry.is_file():
                print('entry is file: ' + depth + entry.path)
                queue.append(entry.path)
                log.write(depth + ' ' + entry.name + '\n')

    @Slot(int)
    def test_clicked(self, clicked):
        print("test clicked!")
        # Dry run: Output log file with changes

        queue = []
        log = open(self.log_file_location, "w+")
        log.write('Starting directory: ' + self.starting_dir_text)
        log.write('Directory tree replacement will be performed on:\n')
        self.add_to_queue(self.starting_dir_text, queue, log)
        for item in queue:
            old_name = os.path.basename(item)
            dir = os.path.dirname(item)
            old_path = dir + os.sep + old_name
            for char in self.chars_to_replace_list:
                new_name = old_name.replace(char, self.char_to_replace_with)
            new_path = dir + os.sep + new_name
            log.write(old_name + ' --> ' + new_name + '\n')
            print('we would call os.rename('+old_path+', '+new_path+')')
        log.close()


    @Slot(int)
    def run_clicked(self, clicked):
        print("run clicked!")
        # Detect OS to determine correct move command and file seperator. \
        # ^ -- This is not necessary as Python's os.rename module is a wrapper for multiple platform modules.
        # Add all files and folders in directory to a queue.
        # Iterate queue.
        # Check if file or folder. If a folder, add contents to queue.
        # System move command to rename file. Replace characters in file name.
        # Log changes in a new line.
        queue = []
        log = open(self.log_file_location, "w+")
        log.write('Starting directory: ' + self.starting_dir_text + '\n')
        log.write('Directory tree replacement will be performed on:\n')
        self.add_to_queue(self.starting_dir_text, queue, log)
        for item in queue:
            old_name = os.path.basename(item)
            dir = os.path.dirname(item)
            old_path = dir + os.sep + old_name
            for char in self.chars_to_replace_list:
                new_name = old_name.replace(char, self.char_to_replace_with)
            new_path = dir + os.sep + new_name
            try:
                os.rename(old_path, new_path)
                log.write(old_name + ' --> ' + new_name + '\n')
            except IOError as err:
                print(err)
        log.close()



if __name__ == '__main__':
    print('test')
    app = QGuiApplication(sys.argv)
    backend = Backend()

    # These are unnecessary and we definitely want to remove the print()
    #backend.starting_dir_changed.connect(lambda text: print(backend.starting_dir_text))
    #backend.chars_to_replace_changed.connect(lambda text: print(backend.chars_to_replace_list))
    #backend.char_to_replace_with_changed.connect(lambda text: print(backend.char_to_replace_with_text))
    #backend.log_file_location_changed.connect(lambda text: print(backend.log_file_location_text))

    engine = QQmlApplicationEngine()
    current_path = os.path.abspath(os.path.dirname(__file__))
    qml_file = os.path.join(current_path, 'view.qml')
    engine.rootContext().setContextProperty("backend", backend)
    engine.load(QUrl(qml_file))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
