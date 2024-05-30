/* global $ */
$(document).ready(() => {
  $('div#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
