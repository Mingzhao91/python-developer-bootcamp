document.addEventListener("DOMContentLoaded", function () {
  const button1 = document.getElementById("myButton");

  function logEvent(event) {
    console.log("Event type: ", event.type);
  }

  button1.addEventListener("click", logEvent);

  function removeElement(event) {
    if (event.key == "Backspace") {
      const nextParagraph = document.getElementsByTagName("p");
      document.body.removeChild(nextParagraph);
    }
  }

  document.addEventListener("keydown", removeElement);
});

function showAlert() {
  const subTitle = document.getElementById("subheader");
  console.log(subTitle);
  const title = document.getElementsByClassName("first-text")[0];
  title.textContent = "second content";
  // replace the whole element
  title.outerHTML = "<p>hello world</p>";
  const paragraphs = document.getElementsByTagName("p");
  alert("button checked!");
}

function changelink() {
  const link = document.getElementById("link");
  link.href = "https://www.wikipedia.org/";
}

// Getting an Element by ID
var element = document.getElementById("example");

// Changing an Element's Style
element.style.color = "red";

// Adding an Event Listener
element.addEventListener("click", function () {
  alert("Hello World!");
});

// ################################################################# note: #################################################################

// Common Ways to Use the DOM
// Here are some common ways to use the DOM:

// Manipulating HTML and CSS
// You can use the DOM to add, delete, and modify elements and attributes in an HTML document. You can also use the DOM to change the style of an HTML element. For example:

var element = document.getElementById("example");

// Adding a new element
var newElement = document.createElement("p");
var text = document.createTextNode("Hello World!");
newElement.appendChild(text);

element.appendChild(newElement);

// Removing an element
var oldElement = document.getElementById("old-example");
element.removeChild(oldElement);

// Modifying an attribute
element.setAttribute("class", "new-class");

// Changing the style
element.style.color = "red";

// Dynamic Content
// You can use the DOM to create dynamic content that changes based on user input or other events. For example:

var button = document.getElementById("example-button");
var container = document.getElementById("example-container");

button.addEventListener("click", function () {
  var newElement = document.createElement("p");
  var text = document.createTextNode("Hello World!");
  newElement.appendChild(text);

  container.appendChild(newElement);
});

// Event Handling
// You can use the DOM to handle user events, such as clicks and mouse movements. For example:

var element = document.getElementById("example");

element.addEventListener("click", function () {
  alert("Hello World!");
});

element.addEventListener("mousemove", function (event) {
  var x = event.clientX;
  var y = event.clientY;

  console.log("Mouse coordinates: " + x + ", " + y);
});
