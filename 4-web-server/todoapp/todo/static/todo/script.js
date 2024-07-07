// document.addEventListener("DOMContentLoaded", function () {});

// document.getElementById("addButton").addEventListener("click", function () {});

const input = document.getElementById("input");
const priority = document.getElementById("priority");
const listsContainer = document.getElementById("lists-container");
const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

function addTask() {
  const task = input.value;
  if (task.trim() === "") {
    return;
  }
  const taskPriority = priority.value;
  const taskItem = document.createElement("li");
  const taskText = document.createElement("span");
  taskText.classList.add("task-text");

  const checkbox = document.createElement("input");
  checkbox.classList.add("form-check-input");
  checkbox.type = "checkbox";

  taskText.textContent = task;
  taskItem.appendChild(checkbox);
  taskItem.appendChild(taskText);
  const taskList = document.getElementById("task-list-" + taskPriority);

  taskList.appendChild(taskItem);
  input.value = "";
}

listsContainer.addEventListener("click", checkBoxClick);

function checkBoxClick(event) {
  console.log(event);

  if (event.target.tagName === "INPUT" && event.target.type === "checkbox") {
    const taskId = event.target.id;
    fetch("/todo/delete_task", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken
      },
      body: JSON.stringify({ taskId: taskId })
    }).catch((error) => {
      console.error("Error:", error);
    });
    const listItem = event.target.parentNode;
    const taskList = listItem.parentNode;
    taskList.removeChild(listItem);
  }
}
