import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QTextEdit
)

class RadarDataProcessorGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        self.setWindowTitle("Radar Data Processor")
        self.setGeometry(200, 200, 600, 400)  # Set window size and position

        main_layout = QHBoxLayout(self)
        
        # Set main window background color
        self.setStyleSheet("background-color: #2C3E50;")  # Dark blue-gray background

        # Left Sidebar Layout
        left_layout = QVBoxLayout()

        # Dropdown for Algorithm
        self.algorithm_label = QLabel("Type of Algorithm:")
        self.algorithm_label.setStyleSheet("color: #ECF0F1; font-size: 14px;")
        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItems(["JPDA", "MUNKRES"])
        self.algorithm_combo.setStyleSheet("background-color: #34495E; color: #ECF0F1;")

        # Dropdown for Filter
        self.filter_label = QLabel("Type of Filter:")
        self.filter_label.setStyleSheet("color: #ECF0F1; font-size: 14px;")
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["CV", "CT", "CA", "IMM"])
        self.filter_combo.setStyleSheet("background-color: #34495E; color: #ECF0F1;")

        # Dropdown for Track Initiation
        self.track_initiation_label = QLabel("Type of Track Initiation:")
        self.track_initiation_label.setStyleSheet("color: #ECF0F1; font-size: 14px;")
        self.track_initiation_combo = QComboBox()
        self.track_initiation_combo.addItems(["2 Step", "3 Step", "4 Step"])
        self.track_initiation_combo.setStyleSheet("background-color: #34495E; color: #ECF0F1;")

        # Dropdown for Plot Type
        self.plot_type_label = QLabel("Type of Plot:")
        self.plot_type_label.setStyleSheet("color: #ECF0F1; font-size: 14px;")
        self.plot_type_combo = QComboBox()
        self.plot_type_combo.addItems([
            "PPI", "C-Scope", "V-Scope", "Time vs Range",
            "Time vs Azimuth", "Time vs Elevation", "Range vs Height"
        ])
        self.plot_type_combo.setStyleSheet("background-color: #34495E; color: #ECF0F1;")

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet(
            "background-color: #1ABC9C; color: white; font-weight: bold; padding: 8px;"
        )
        self.submit_button.clicked.connect(self.submit_clicked)

        # Add widgets to left layout
        left_layout.addWidget(self.algorithm_label)
        left_layout.addWidget(self.algorithm_combo)
        left_layout.addWidget(self.filter_label)
        left_layout.addWidget(self.filter_combo)
        left_layout.addWidget(self.track_initiation_label)
        left_layout.addWidget(self.track_initiation_combo)
        left_layout.addWidget(self.plot_type_label)
        left_layout.addWidget(self.plot_type_combo)
        left_layout.addWidget(self.submit_button)

        # Output Box (Right Side)
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: #34495E; color: #ECF0F1; font-size: 14px;")

        # Add layouts to main layout
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.output_box)

    def submit_clicked(self):
        # Get selected options
        algorithm = self.algorithm_combo.currentText()
        filter_type = self.filter_combo.currentText()
        track_initiation = self.track_initiation_combo.currentText()
        plot_type = self.plot_type_combo.currentText()

        # Format output message
        output_message = (
            f"Algorithm: {algorithm}\n"
            f"Filter: {filter_type}\n"
            f"Track Initiation: {track_initiation}\n"
            f"Plot Type: {plot_type}\n"
        )

        # Display the output
        self.output_box.setText(output_message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RadarDataProcessorGUI()
    window.show()
    sys.exit(app.exec_())
