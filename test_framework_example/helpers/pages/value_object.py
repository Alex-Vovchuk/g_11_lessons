class UserCredentials:
    def __init__(self, first_name, last_name, gender, email, phone_number, adult=True):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.adult = adult


class Builder:
    def __init__(self):
        self.result = {}

    def add_string(self, key, value):
        self.result[key] = value
        return self

    def add_boolean(self, key='adult', value=True):
        self.result[key] = value
        return self

    def add_array(self, key, values):
        # for i in range(len(values)):
        #     self.result[key+i] = values[i]
        self.result[key] = list(values)
        return self

    def build(self):
        return self.result

    def clear(self):
        self.result = {}
        return self.result


class CredentialBuilder(Builder):

    def add_first_name(self, first_name):
        self.result['first_name'] = first_name

    def add_hobbies(self, hobbies_list):
        for i in range(len(hobbies_list)):
            self.result['hobbies' + str(i)] = hobbies_list[i]

    def add_adult(self, adult):
        if not adult:
            self.add_boolean('adult', )

#
# class BookBuilder(Builder):
#     pass