class GSTCases:

    @staticmethod
    def calc_gst(i):
        return i * 0.15

    @staticmethod
    def add_gst(i):
        return i + (i * 0.15)

    @staticmethod
    def gst_comp(i):
        return i * (3 / 23)

    @staticmethod
    def gst_excl(i):
        return i / 1.15

    @staticmethod
    def print_stars():
        return "*" * 100


# Main routine
print(GSTCases.print_stars())
print(f"GST on $100 is ${GSTCases.calc_gst(100)}")
print(f"so adding GST to $100 is ${GSTCases.add_gst(100)}")
print(GSTCases.print_stars())
print(f"If the GST inclusive price is $10,350, the GST amount is $"
      f"{GSTCases.gst_comp(10350)}")
print(f"so the GST exclusive amount is ${GSTCases.gst_excl(10350)}")
print(GSTCases.print_stars())
