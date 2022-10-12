import dictionary as d
import txt_converter as t

def view():
    data = d.add_contact()
    t.converter(data)
    return data