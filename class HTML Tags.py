import io

#
# class HtmlTag:
#     def __init__(self, name: str, attributes: dict, style: dict, closer_subtag: bool = True):
#         # TAG NAME
#         self.__name = name.upper()
#         # Does tag have close part like <HTML></HTML>?
#         self.closer_subtag = closer_subtag
#         # HTML Tag attributes
#         self.attributes = attributes
#         # HTML TAG CSS style
#         self.style = style
#         # Body between subtag
#         self.__content = io.StringIO()
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name:str):
#         self.__name = new_name
#         print("name successfully changed")
#
#     @property
#     def content(self):
#         return self.__content.getvalue()
#
#     # @content.setter
#     # def content(self, new_str:str):
#     #     self.__content.write(new_str)
#
#     #Setting HTML Tag attribute
#     def set_attribute(self, attribute_name:str, attribute_value:str):
#         self.attributes[attribute_name] = attribute_value
#
#
#     #Set a new CSS style
#     def set_style(self, style_name:str, style_value:str):
#         self.style[style_name] = style_value
#
#     #Add content into the text
#     def add_content(self, content:str):
#         self.__content.write(content)
#         print("new content has successfully added")
#
#     #Clear content
#     def clear_content(self):
#         self.__content = io.StringIO()
#
#     #SHOW TAG as is
#     def show(self):
#         tag_io = io.StringIO()
#         opening = r'<'
#         close_opening = r'</'
#         closing = r">"
#         tag_io.write(f'{opening}{self.name}')
#
# # <IMG attr1=attr1_value" attr2=attr2_value style="; style1:style1_value; style2:style2_value> CONTENTCONTENTCONTENT</img>
#
#         if self.attributes:
#             tag_io.write(' ' + ' '.join([f'{attr_key}="{self.attributes[attr_key]}"' for attr_key in self.attributes]))
#
#         if self.style:
#             tag_io.write(' style="' + '; '.join([f'{style_key}: {self.style[style_key]}' for style_key in self.style]))
#
#         tag_io.write(closing)
#
#         if self.closer_subtag:
#             tag_io.write(self.content)
#             tag_io.write(f'{close_opening}{self.name}{closing}')
#
#         return tag_io.getvalue()
#
# class Style(HtmlTag):
#     def __init__(self, attributes:dict, style: dict):
#         super().__init__(name="style",attributes=attributes, style=style, closer_subtag=True )
#
# a = HtmlTag("img", {"attr1":"attr1_value", "attr2":"attr2_value"}, {"style1":"style1_value", "style2":"style2_value"})
# a.add_content("Testing Html_tag")
# print(a.show())
# print("--------------STYLE")
# s = Style({"attr1":"attr1_value", "attr2":"attr2_value"}, {"style1":"style1_value", "style2":"style2_value"})
# print(s.show())
# s2 = Style({"attr1":"attr1_value", "attr2":"attr2_value"}, {"style1":"style1_value", "style2":"style2_value"})







