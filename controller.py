import model
import view

def start():
    x = view.show_menu()
    if x == 1:
        view.print_person(model.find_persone(view.find_person()))
    elif x == 2:
        view.print_person(model.filter_of_position(view.filter_of_position()))
    elif x == 3:
        salary = view.filter_of_salary()
        view.print_person(model.filter_of_salary(salary[0], salary[1]))
    elif x == 4:
        model.add_person(view.add_person(model.init()))
    elif x == 5:
        model.del_person(view.del_person())
    elif x == 6:
        model.change_person(view.change_person())
    elif x == 7:
        model.export_json(view.export_json())
    elif x == 8:
        model.export_csv(view.export_csv())
    elif x == 9:
        view.stop()
        return False
    elif x == 10:
        model.import_csv(view.import_csv())
    else:
        view.error_command()
    return True