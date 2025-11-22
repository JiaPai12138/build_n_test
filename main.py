import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("PyQt5 WebEngine 示例")
        # 设置窗口大小
        self.resize(1024, 768)

        # 创建Web引擎视图
        self.browser = QWebEngineView()
        # 加载指定网页（这里以百度为例）
        self.browser.load(QUrl("https://www.baidu.com"))
        # 将浏览器设置为主窗口的中央部件
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    # 确保应用程序初始化
    app = QApplication(sys.argv)
    # 创建并显示窗口
    window = WebBrowser()
    window.show()
    # 进入应用程序事件循环
    sys.exit(app.exec_())