from modules._module import Module
from utils.core.dataset import Option
import qrcode


# 继承module父类
class HomeModule(Module):
    def __init__(self):
        # 输出信息
        information = {"Name": "QR Generator",
                       "Description": "With this module it is possible to generate a QR code in a customized way according to the information provided.",
                       "OS": "Linux",
                       "Author": "@Mans00r"}
        # 模块参数
        options = {
            'data': Option.create(name="data", required=True, description="data to write"),
            'version': Option.create(name="version", value=1, required=False, description="version of qr generated"),
            'box_size': Option.create(name="data", value=10, required=False, description="size of the box of the qr"),
            'border': Option.create(name="data", value=1, required=False, description="width of the border"),
            'fill_color': Option.create(name="fill_color", value="black", required=False,
                                        description="color of the pattern"),
            'back_color': Option.create(name="back_color", value="white", required=False,
                                        description="background color"),
            'append': Option.create(name="append", value=False, required=True,
                                    description="overwrite the records of a tag"),
            'file': Option.create(name="file", value="qr.png", required=True, description="destination file"),
            'save': Option.create(name="save", value=False,
                                  description="Weather if we save the file in the path written in file or not"),
        }

        super(HomeModule, self).__init__(information, options)

    # 必须实现run方法
    def run(self):
        # 拿到args值
        data = self.args.get("data", "")
        version = int(self.args.get("version", 1))  # 1～40
        box_size = int(self.args.get("box_size", 10))
        border = int(self.args.get("border", 1))
        fill_color = self.args.get("fill_color", "black")
        back_color = self.args.get("back_color", "white")
        save = str(self.args.get("save", "False")).lower() == "true"
        path = self.args.get("file", "qr.png")
        if "/" not in path:
            path = f"./files/{path}"

        self.create_qr(data, version, box_size, border, fill_color, back_color, save, path)

    # 模块具体处理函数
    @staticmethod
    def create_qr(data, version, box_size, border, fill_color, back_color, save, path):
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.show()

        if save:
            img.save(path)

        # TODO: Subsequent related operations of qrcode
        # TODO: Applied to phishing attacks
