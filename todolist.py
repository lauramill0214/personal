let tasks = [];

function addTask() {
    let task = prompt("Enter a task:");
    tasks.push(task);
    displayTasks();
}

function deleteTask() {
    let index = prompt("Enter the index of the task to delete:");
    tasks.splice(index, 1);
    displayTasks();
}

function completeTask() {
    let index = prompt("Enter the index of the task to mark as completed:");
    tasks[index] = tasks[index] + " (completed)";
    displayTasks();
}

function displayTasks() {
    console.clear();
    console.log("To-Do List:");
    for (let i = 0; i < tasks.length; i++) {
        console.log(i + ": " + tasks[i]);
    }
}

while (true) {
    let choice = prompt("Enter 1 to add a task, 2 to delete a task, 3 to mark a task as completed, or 0 to quit:");
    if (choice == "1") {
        addTask();
    } else if (choice == "2") {
        deleteTask();
    } else if (choice == "3") {
        completeTask();
    } else if (choice == "0") {
        break;
    } else {
        console.log("Invalid choice");
    }
}
