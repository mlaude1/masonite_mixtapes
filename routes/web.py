"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    
    RouteGroup([
        Get("/", "MixtapeController@index").name("index"),
        Get("/@id", "MixtapeController@show").name("show"),
        Post("/", "MixtapeController@create").name("create"),
        Put("/@id", "MixtapeController@update").name("update"),
        Delete("/@id", "MixtapeController@destroy").name("destroy")
    ], prefix="/mixtape", name="mixtape")
]
