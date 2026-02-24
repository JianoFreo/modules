// Example: Load students from JSON (Node.js)
const students = require('./Database_temp/studentClass.json');

// Print the first student's name and the second student's gpa (if available)
console.log(students[0].name); // array 0 is student 1
console.log(students[1]?.gpa); // array 1 is student 2, using optional chaining to avoid errors
//------------------------------------------------------------------------------------------------------------
// Example: Display students in the browser (Browser)       
// const appDiv = document.getElementById('app');
// students.forEach(student => {
//     const studentInfo = document.createElement('p');
//     studentInfo.textContent = `Name: ${student.name}, GPA: ${student.gpa ?? 'N/A'}`; // using nullish coalescing to handle undefined gpa
//     appDiv.appendChild(studentInfo);
// });
//------------------------------------------------------------------------------------------------------------
// Example: Print all students' names and GPAs to the console (Node.js)
students.forEach(student => {
    console.log(`Name: ${student.name}, GPA: ${student.gpa ?? 'N/A'}`);
});
//------------------------------------------------------------------------------------------------------------
// Simple example: Print numbers 1-3 to the console
[1, 2, 3].forEach(num => {
    console.log(`Number: ${num}`);
});
//------------------------------------------------------------------------------------------------------------
//lambda function example or fat arrow function
studentGrades = (gpa1, gpa2) => console.log(gpa1 + gpa2);

//calling the function
studentGrades(Math.round(students[0].gpa), Math.round(students[1].gpa));
studentGrades(Math.round(students[0].gpa), Math.round(students[2].gpa));