import React, { useState } from 'react';
import StudentItem from '/workspaces/test/my-app11/src/components/StudentItem.jsx';

const StudentList = () => {
  const [students, setStudents] = useState([]);

  const addStudent = (student) => {
    setStudents([...students, student]);
  };

  const removeStudent = (id) => {
    setStudents(students.filter((s) => s.id !== id));
  };

  return (
    <div>
      <h2>Список студентов</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Имя</th>
            <th scope="col">Возраст</th>
            <th scope="col">Курс</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <StudentItem key={student.id} student={student} onRemove={removeStudent} />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StudentList;