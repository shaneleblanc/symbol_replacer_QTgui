import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtQuick.Dialogs 1.0


Window {
    id: window
    visible: true
    width: 360
    height: 300
    title: qsTr("Symbol Replacer 0.1")

    Text {
        id: element
        x: 18
        y: 17
        text: qsTr("Select the directory:")
        font.pixelSize: 12
    }

    Text {
        id: element1
        x: 18
        y: 82
        text: qsTr("Enter the characters to replace (comma seperated):")
        font.pixelSize: 12
    }

    Text {
        id: element2
        x: 18
        y: 143
        text: qsTr("Enter one character to replace with:")
        font.pixelSize: 12
    }

    Button {
        id: test_button
        x: 70
        y: 266
        onClicked: {
            backend.test_clicked(1)
        }
        text: qsTr("Test")
    }

    TextField {
        id: starting_dir_textfield
        x: 18
        y: 38
        width: 318
        height: 30
        onTextChanged: backend.starting_dir = starting_dir_textfield.text
        placeholderText: qsTr("Text Field")
    }

    TextField {
        id: chars_to_replace_textfield
        x: 18
        y: 103
        width: 318
        height: 30
        placeholderText: qsTr("Text Field")
        onTextChanged: backend.chars_to_replace = chars_to_replace_textfield.text
    }

    TextField {
        id: char_to_replace_with_textfield
        x: 18
        y: 164
        width: 36
        height: 34
        maximumLength: 1
        placeholderText: qsTr("Text Field")
        onTextChanged: backend.char_to_replace_with = chars_to_replace_textfield.text
    }

    Button {
        id: run_button
        x: 210
        y: 266
        text: qsTr("Run")
        onClicked: {
            backend.run_clicked(1)
        }
    }

    Text {
        id: element3
        x: 18
        y: 204
        text: qsTr("Output log file to:")
        font.pixelSize: 12
    }

    TextField {
        id: log_file_textfield
        x: 18
        y: 225
        width: 318
        height: 30
        placeholderText: qsTr("Text Field")
    }
}

