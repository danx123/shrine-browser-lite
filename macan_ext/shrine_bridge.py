from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal

class ShrineBridge(QObject):
    messageReceived = pyqtSignal(str)

    @pyqtSlot(str)
    def receiveMessage(self, msg):
        print(f"[ShrineBridge] Msg from JS: {msg}")
        self.messageReceived.emit(msg)
