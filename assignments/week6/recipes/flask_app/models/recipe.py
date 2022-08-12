DB = "user"

class Recipe:
    def __init__(self, recipe):
        self.id = recipe["id"]
        self.name = recipe["name"]
        self.description = recipe["description"]
        self.instructions = recipe["instructions"]
        self.dateCooked = recipe["dateCooked"]
        self.under30 = recipe["under30"]
        self.created_at = recipe["created_at"]
        self.updated_at = recipe["updated_at"]
        self.user = None

    def recipeName(self):
        return f'{self.name}:'

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM recipe;'
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes

    @classmethod
    def getOne(cls, data):
        query = 'SELECT * FROM recipe WHERE id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # @classmethod
    # def getEmail(cls, data):
    #     query = "SELECT * FROM user WHERE email = %(email)s;"
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     if len(results) < 1:
    #         return False
    #     return cls(results[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (name, description, instructions, under30, dateCooked, userID) VALUES (%(name)s, %(description)s, %(instructions)s, %(under30)s, %(dateCooked)s, %(user_id)s,);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass