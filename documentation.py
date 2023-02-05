import justpy as jp


class Doc:

    def serve(self):
        wp = jp.WebPage()
        mainDiv = jp.Div(a=wp, classes="bg-gray-100 h-screen font-mono")

        jp.Div(a=mainDiv,
               text="Instant Dictionary API",
               classes="text-4xl mx-4")
        jp.Div(a=mainDiv,
               text="Get Definition of words",
               classes="text-lg m-4")

        jp.Hr(a=mainDiv)
        jp.Div(a=mainDiv,
               text="www.example.com/api?w=moon", #put your domain webpage
               )
        jp.Hr(a=mainDiv)
        jp.Div(a=mainDiv,
               text=""" {"word:"moon","definition":
               ["A natural satellite a planet",
               "A month, particularly a lunar month (approximately 28 days).",
               "To fuss over adoringly or with great affection.",
               "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).",
               "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."]}
               """)
        return wp
