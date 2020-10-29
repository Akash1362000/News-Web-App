var instance = M.Carousel.init({
    fullWidth: true
  });
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {hover: true, closeOnClick: true, inDuration: 350, outDuration: 400, constrainWidth: true, container: null   });
  });

var collapsibleElem = document.querySelector('.collapsible');
var collapsibleInstance = M.Collapsible.init(collapsibleElem, options);

