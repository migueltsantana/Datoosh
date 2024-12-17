var termynals = document.getElementsByClassName("termynal");
for (var i = 0; i < termynals.length; i++) {
   new Termynal(termynals.item(i));
}