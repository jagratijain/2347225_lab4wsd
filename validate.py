from lxml import etree

def validate_xml(xml_filename, xsd_filename):
    try:
        # Load the XML file and the XSD schema
        xml_doc = etree.parse(xml_filename)
        xsd_doc = etree.parse(xsd_filename)

        # Create a schema object and validate the XML against the schema
        schema = etree.XMLSchema(xsd_doc)
        is_valid = schema.validate(xml_doc)

        if is_valid:
            print(f"{xml_filename} is valid according to {xsd_filename}.")
        else:
            print(f"{xml_filename} is NOT valid according to {xsd_filename}.")
            print("Validation errors:")
            for error in schema.error_log:
                print(error)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    xml_file = "2347225lab4.xml"  # Replace with your XML file's name
    xsd_file = "2347225_lab4.xsd"  # Replace with your XSD schema file's name
    validate_xml(xml_file, xsd_file)