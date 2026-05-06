####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Enumerations
Genre: Enumeration = Enumeration(
    name="Genre",
    literals={
            EnumerationLiteral(name="Poetry"),
			EnumerationLiteral(name="Thriller"),
			EnumerationLiteral(name="History"),
			EnumerationLiteral(name="Technology"),
			EnumerationLiteral(name="Romance"),
			EnumerationLiteral(name="Horror"),
			EnumerationLiteral(name="Adventure"),
			EnumerationLiteral(name="Philosophy"),
			EnumerationLiteral(name="Cookbooks"),
			EnumerationLiteral(name="Fantasy")
    }
)

# Classes
Book = Class(name="Book")
Library = Class(name="Library")
Author = Class(name="Author")

# Book class attributes and methods
Book_title: Property = Property(name="title", type=StringType)
Book_pages: Property = Property(name="pages", type=IntegerType)
Book_stock: Property = Property(name="stock", type=IntegerType)
Book_price: Property = Property(name="price", type=FloatType)
Book_release: Property = Property(name="release", type=DateType)
Book_genre: Property = Property(name="genre", type=Genre)
Book_m_decrease_stock: Method = Method(name="decrease_stock", parameters={Parameter(name='qty', type=IntegerType)}, implementation_type=MethodImplementationType.CODE)
Book_m_decrease_stock.code = """def decrease_stock(self, qty: int):
    \"\"\"
    Decrease the available stock by the given quantity.

    :param qty: Number of items to remove from stock
    :raises ValueError: If qty is negative or exceeds available stock
    \"\"\"
    if qty <= 0:
        raise ValueError("Quantity must be a positive integer")

    if qty > self.stock:
        raise ValueError(
            f"Cannot decrease stock by {qty}. Only {self.stock} items available."
        )

    self.stock -= qty

"""
Book.attributes={Book_genre, Book_pages, Book_price, Book_release, Book_stock, Book_title}
Book.methods={Book_m_decrease_stock}

# Library class attributes and methods
Library_name: Property = Property(name="name", type=StringType)
Library_web_page: Property = Property(name="web_page", type=StringType)
Library_address: Property = Property(name="address", type=StringType)
Library_telephone: Property = Property(name="telephone", type=StringType)
Library_m_cheapest_book_by: Method = Method(name="cheapest_book_by", parameters={Parameter(name='author', type=Author)}, type=StringType, implementation_type=MethodImplementationType.BAL)
Library_m_cheapest_book_by.code = """def cheapest_book_by(author:Author) -> str {
    cheapest:Book = null;
	price = 1000000000.0;
	for(book in this.books){
        if(book.authors.contains(author)
			&& book.price <= price){
            cheapest = book;
			price = book.price;
		}
    }
	return cheapest.title;
}"""
Library.attributes={Library_address, Library_name, Library_telephone, Library_web_page}
Library.methods={Library_m_cheapest_book_by}

# Author class attributes and methods
Author_name: Property = Property(name="name", type=StringType)
Author_birth: Property = Property(name="birth", type=DateType)
Author.attributes={Author_birth, Author_name}

# Relationships
books: BinaryAssociation = BinaryAssociation(
    name="books",
    ends={
        Property(name="library", type=Library, multiplicity=Multiplicity(1, 9999)),
        Property(name="books", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)
books_1: BinaryAssociation = BinaryAssociation(
    name="books_1",
    ends={
        Property(name="authors", type=Author, multiplicity=Multiplicity(1, 9999)),
        Property(name="books", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)


# OCL Constraints
constraint_Book_0_1: Constraint = Constraint(
    name="constraint_Book_0_1",
    context=Book,
    expression="context Book inv inv1: self.pages> 10",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Book, Library, Author, Genre},
    associations={books, books_1},
    constraints={constraint_Book_0_1},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="Book", view_elements=set(), is_main_page=True, route_path="/book", screen_size="Medium")
wrapper.component_id = "page-book-0"
ih938 = Text(
    name="ih938",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ih938",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ih938"}
)
i096i = Link(
    name="i096i",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i096i",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "i096i"}
)
i2dew = Link(
    name="i2dew",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i2dew",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i2dew"}
)
ipty2 = Link(
    name="ipty2",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ipty2",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "ipty2"}
)
ihh75 = ViewContainer(
    name="ihh75",
    description=" component",
    view_elements={i096i, i2dew, ipty2},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="ihh75",
    display_order=1,
    custom_attributes={"id": "ihh75"}
)
ihh75_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
ihh75.layout = ihh75_layout
i69gz = Text(
    name="i69gz",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i69gz",
    display_order=2,
    custom_attributes={"id": "i69gz"}
)
iauxg = ViewContainer(
    name="iauxg",
    description="nav container",
    view_elements={ih938, ihh75, i69gz},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iauxg",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iauxg"}
)
iauxg_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iauxg.layout = iauxg_layout
iimww = Text(
    name="iimww",
    content="Book",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iimww",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iimww"}
)
ibfkp = Text(
    name="ibfkp",
    content="Manage Book data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="ibfkp",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ibfkp"}
)
table_book_0_col_0 = FieldColumn(label="Title", field=Book_title)
table_book_0_col_1 = FieldColumn(label="Pages", field=Book_pages)
table_book_0_col_2 = FieldColumn(label="Stock", field=Book_stock)
table_book_0_col_3 = FieldColumn(label="Price", field=Book_price)
table_book_0_col_4 = FieldColumn(label="Release", field=Book_release)
table_book_0_col_5 = FieldColumn(label="Genre", field=Book_genre)
table_book_0_col_6_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "library")
table_book_0_col_6 = LookupColumn(label="Library", path=table_book_0_col_6_path, field=Library_name)
table_book_0_col_7_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "authors")
table_book_0_col_7 = LookupColumn(label="Authors", path=table_book_0_col_7_path, field=Author_name)
table_book_0 = Table(
    name="table_book_0",
    title="Book List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_book_0_col_0, table_book_0_col_1, table_book_0_col_2, table_book_0_col_3, table_book_0_col_4, table_book_0_col_5, table_book_0_col_6, table_book_0_col_7],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-book-0",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Book List", "data-source": "class_oho5ergc3_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'title', 'label': 'Title', 'columnType': 'field', '_expanded': False}, {'field': 'pages', 'label': 'Pages', 'columnType': 'field', '_expanded': False}, {'field': 'stock', 'label': 'Stock', 'columnType': 'field', '_expanded': False}, {'field': 'price', 'label': 'Price', 'columnType': 'field', '_expanded': False}, {'field': 'release', 'label': 'Release', 'columnType': 'field', '_expanded': False}, {'field': 'genre', 'label': 'Genre', 'columnType': 'field', '_expanded': False}, {'field': 'library', 'label': 'Library', 'columnType': 'lookup', 'lookupEntity': 'class_06blhjj3h_mjikkmod', 'lookupField': 'name', '_expanded': False}, {'field': 'authors', 'label': 'Authors', 'columnType': 'lookup', 'lookupEntity': 'class_d3f0di6lb_mjikkmoe', 'lookupField': 'name', '_expanded': False}], "id": "table-book-0", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_book_0_binding_domain = None
if domain_model_ref is not None:
    table_book_0_binding_domain = domain_model_ref.get_class_by_name("Book")
if table_book_0_binding_domain:
    table_book_0_binding = DataBinding(domain_concept=table_book_0_binding_domain, name="BookDataBinding")
else:
    # Domain class 'Book' not resolved; data binding skipped.
    table_book_0_binding = None
if table_book_0_binding:
    table_book_0.data_binding = table_book_0_binding
id22m = Button(
    name="id22m",
    description="Button component",
    label="+ decrease_stock",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Book_m_decrease_stock,
    instance_source="table-book-0",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="id22m",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ decrease_stock", "data-action-type": "run-method", "data-method": "method_rb01uirsh_mjikkmod", "data-instance-source": "table-book-0", "id": "id22m", "method-class": "Book", "endpoint": "/book/{book_id}/methods/decrease_stock/", "is-instance-method": "true", "input-parameters": {'qty': {'type': 'int', 'required': True}}, "instance-source": "table-book-0"}
)
iafwr = ViewContainer(
    name="iafwr",
    description=" component",
    view_elements={id22m},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="iafwr",
    display_order=3,
    custom_attributes={"id": "iafwr"}
)
iafwr_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
iafwr.layout = iafwr_layout
iyd75 = ViewContainer(
    name="iyd75",
    description="main container",
    view_elements={iimww, ibfkp, table_book_0, iafwr},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="iyd75",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "iyd75"}
)
iyd75_layout = Layout(flex="1")
iyd75.layout = iyd75_layout
ihvpi = ViewContainer(
    name="ihvpi",
    description=" component",
    view_elements={iauxg, iyd75},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="ihvpi",
    display_order=0,
    custom_attributes={"id": "ihvpi"}
)
ihvpi_layout = Layout(layout_type=LayoutType.FLEX)
ihvpi.layout = ihvpi_layout
wrapper.view_elements = {ihvpi}


# Screen: wrapper_2
wrapper_2 = Screen(name="wrapper_2", description="Library", view_elements=set(), route_path="/library", screen_size="Medium")
wrapper_2.component_id = "page-library-1"
ivclw = Text(
    name="ivclw",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ivclw",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ivclw"}
)
i9iog = Link(
    name="i9iog",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i9iog",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "i9iog"}
)
i9rkj = Link(
    name="i9rkj",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i9rkj",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i9rkj"}
)
i4dqx = Link(
    name="i4dqx",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i4dqx",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "i4dqx"}
)
itcr1 = ViewContainer(
    name="itcr1",
    description=" component",
    view_elements={i9iog, i9rkj, i4dqx},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="itcr1",
    display_order=1,
    custom_attributes={"id": "itcr1"}
)
itcr1_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
itcr1.layout = itcr1_layout
idcdh = Text(
    name="idcdh",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="idcdh",
    display_order=2,
    custom_attributes={"id": "idcdh"}
)
ipbbl = ViewContainer(
    name="ipbbl",
    description="nav container",
    view_elements={ivclw, itcr1, idcdh},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="ipbbl",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "ipbbl"}
)
ipbbl_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
ipbbl.layout = ipbbl_layout
ir2sj = Text(
    name="ir2sj",
    content="Library",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ir2sj",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ir2sj"}
)
igpec = Text(
    name="igpec",
    content="Manage Library data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="igpec",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "igpec"}
)
table_library_1_col_0 = FieldColumn(label="Name", field=Library_name)
table_library_1_col_1 = FieldColumn(label="Web Page", field=Library_web_page)
table_library_1_col_2 = FieldColumn(label="Address", field=Library_address)
table_library_1_col_3 = FieldColumn(label="Telephone", field=Library_telephone)
table_library_1_col_4_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "books")
table_library_1_col_4 = LookupColumn(label="Books", path=table_library_1_col_4_path, field=Book_title)
table_library_1 = Table(
    name="table_library_1",
    title="Library List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_library_1_col_0, table_library_1_col_1, table_library_1_col_2, table_library_1_col_3, table_library_1_col_4],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-library-1",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Library List", "data-source": "class_06blhjj3h_mjikkmod", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'web_page', 'label': 'Web Page', 'columnType': 'field', '_expanded': False}, {'field': 'address', 'label': 'Address', 'columnType': 'field', '_expanded': False}, {'field': 'telephone', 'label': 'Telephone', 'columnType': 'field', '_expanded': False}, {'field': 'books', 'label': 'Books', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-library-1", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_library_1_binding_domain = None
if domain_model_ref is not None:
    table_library_1_binding_domain = domain_model_ref.get_class_by_name("Library")
if table_library_1_binding_domain:
    table_library_1_binding = DataBinding(domain_concept=table_library_1_binding_domain, name="LibraryDataBinding")
else:
    # Domain class 'Library' not resolved; data binding skipped.
    table_library_1_binding = None
if table_library_1_binding:
    table_library_1.data_binding = table_library_1_binding
iefrs = Button(
    name="iefrs",
    description="Button component",
    label="+ cheapest_book_by",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.RunMethod,
    method_btn=Library_m_cheapest_book_by,
    instance_source="table-library-1",
    is_instance_method=True,
    styling=Styling(size=Size(padding="6px 14px", font_size="13px", font_weight="600", text_decoration="none", letter_spacing="0.01em"), position=Position(display="inline-flex", cursor="pointer", transition="background 0.2s"), color=Color(background_color="linear-gradient(90deg, #2563eb 0%, #1e40af 100%)", text_color="#fff", color_palette="default", border_radius="4px", border="none", box_shadow="0 1px 4px rgba(37,99,235,0.10)"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center")),
    component_id="iefrs",
    tag_name="button",
    display_order=0,
    css_classes=["action-button-component"],
    custom_attributes={"type": "button", "data-button-label": "+ cheapest_book_by", "data-action-type": "run-method", "data-method": "35ef5329-889b-40f0-89ce-9836936fd8a9", "data-instance-source": "table-library-1", "id": "iefrs", "method-class": "Library", "endpoint": "/library/{library_id}/methods/cheapest_book_by/", "is-instance-method": "true", "input-parameters": {'author': {'type': 'Author', 'required': True, 'input_kind': 'lookup', 'entity': 'Author', 'lookup_field': 'name'}}, "instance-source": "table-library-1"}
)
i68zl = ViewContainer(
    name="i68zl",
    description=" component",
    view_elements={iefrs},
    styling=Styling(size=Size(margin_top="20px"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")),
    component_id="i68zl",
    display_order=3,
    custom_attributes={"id": "i68zl"}
)
i68zl_layout = Layout(layout_type=LayoutType.FLEX, flex_wrap="wrap", gap="10px")
i68zl.layout = i68zl_layout
ikuwz = ViewContainer(
    name="ikuwz",
    description="main container",
    view_elements={ir2sj, igpec, table_library_1, i68zl},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ikuwz",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ikuwz"}
)
ikuwz_layout = Layout(flex="1")
ikuwz.layout = ikuwz_layout
iqwux = ViewContainer(
    name="iqwux",
    description=" component",
    view_elements={ipbbl, ikuwz},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="iqwux",
    display_order=0,
    custom_attributes={"id": "iqwux"}
)
iqwux_layout = Layout(layout_type=LayoutType.FLEX)
iqwux.layout = iqwux_layout
wrapper_2.view_elements = {iqwux}


# Screen: wrapper_3
wrapper_3 = Screen(name="wrapper_3", description="Author", view_elements=set(), route_path="/author", screen_size="Medium")
wrapper_3.component_id = "page-author-2"
i4kvi = Text(
    name="i4kvi",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i4kvi",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i4kvi"}
)
i77rz = Link(
    name="i77rz",
    description="Link element",
    label="Book",
    url="/book",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i77rz",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/book", "id": "i77rz"}
)
i4uiu = Link(
    name="i4uiu",
    description="Link element",
    label="Library",
    url="/library",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i4uiu",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/library", "id": "i4uiu"}
)
ihg2t = Link(
    name="ihg2t",
    description="Link element",
    label="Author",
    url="/author",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ihg2t",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/author", "id": "ihg2t"}
)
i78hn = ViewContainer(
    name="i78hn",
    description=" component",
    view_elements={i77rz, i4uiu, ihg2t},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="i78hn",
    display_order=1,
    custom_attributes={"id": "i78hn"}
)
i78hn_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
i78hn.layout = i78hn_layout
idime = Text(
    name="idime",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="idime",
    display_order=2,
    custom_attributes={"id": "idime"}
)
i78p2 = ViewContainer(
    name="i78p2",
    description="nav container",
    view_elements={i4kvi, i78hn, idime},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i78p2",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i78p2"}
)
i78p2_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i78p2.layout = i78p2_layout
ikopl = Text(
    name="ikopl",
    content="Author",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ikopl",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ikopl"}
)
imo3c = Text(
    name="imo3c",
    content="Manage Author data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="imo3c",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "imo3c"}
)
table_author_2_col_0 = FieldColumn(label="Name", field=Author_name)
table_author_2_col_1 = FieldColumn(label="Birth", field=Author_birth)
table_author_2_col_2_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "books")
table_author_2_col_2 = LookupColumn(label="Books", path=table_author_2_col_2_path, field=Book_title)
table_author_2 = Table(
    name="table_author_2",
    title="Author List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_author_2_col_0, table_author_2_col_1, table_author_2_col_2],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-author-2",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Author List", "data-source": "class_d3f0di6lb_mjikkmoe", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'name', 'label': 'Name', 'columnType': 'field', '_expanded': False}, {'field': 'birth', 'label': 'Birth', 'columnType': 'field', '_expanded': False}, {'field': 'books', 'label': 'Books', 'columnType': 'lookup', 'lookupEntity': 'class_oho5ergc3_mjikkmod', 'lookupField': 'title', '_expanded': False}], "id": "table-author-2", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_author_2_binding_domain = None
if domain_model_ref is not None:
    table_author_2_binding_domain = domain_model_ref.get_class_by_name("Author")
if table_author_2_binding_domain:
    table_author_2_binding = DataBinding(domain_concept=table_author_2_binding_domain, name="AuthorDataBinding")
else:
    # Domain class 'Author' not resolved; data binding skipped.
    table_author_2_binding = None
if table_author_2_binding:
    table_author_2.data_binding = table_author_2_binding
ijpl7 = ViewContainer(
    name="ijpl7",
    description="main container",
    view_elements={ikopl, imo3c, table_author_2},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ijpl7",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ijpl7"}
)
ijpl7_layout = Layout(flex="1")
ijpl7.layout = ijpl7_layout
inyd8 = ViewContainer(
    name="inyd8",
    description=" component",
    view_elements={i78p2, ijpl7},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="inyd8",
    display_order=0,
    custom_attributes={"id": "inyd8"}
)
inyd8_layout = Layout(layout_type=LayoutType.FLEX)
inyd8.layout = inyd8_layout
wrapper_3.view_elements = {inyd8}

gui_module = Module(
    name="GUI_Module",
    screens={wrapper, wrapper_2, wrapper_3}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
