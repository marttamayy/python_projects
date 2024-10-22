capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

#Nested

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],

# }

# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "num_visited": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],

    },

    "Germany": {

        "num_visited": 5,
        "cities_visited": ["Berlin","Hamburg", "Stuttgart"],

    }
}

print(travel_log["Germany"]["cities_visited"][2])