from fpdf import FPDF


class CS50Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def create_shirtificate(self, name, output_filename):
        self.set_auto_page_break(auto=True, margin=15)

        self.add_page()

        self.set_font("Arial", size=20)

        center_x = self.w / 2
        center_y = self.h / 2

        shirt_image = "shirtificate.png"
        self.image(shirt_image, x=center_x - 50, y=center_y - 50, w=100)

        self.set_text_color(255, 255, 255)  # White text
        self.text(center_x - 5, center_y - 20, name)

        self.output(output_filename)


def main():
    name = input("Enter your name: ")
    pdf = CS50Shirtificate()
    pdf.create_shirtificate(name, "shirtificate.pdf")


if __name__ == "__main__":
    main()
