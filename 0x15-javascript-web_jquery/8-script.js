$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json',
    function (films) {
      $.each(films.results, function(index, film) {
        $('#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  );
});
