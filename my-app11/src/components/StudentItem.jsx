import React from 'react';

const StudentItem = ({ student, onRemove }) => {
  const { id, name, age, course } = student;

  const handleRemove = () => {
    onRemove(id);
  };

  return (
    <tr>
      <td>{id}</td>
      <td>{name}</td>
      <td>{age}</td>
      <td>{course}</td>
      <td><button className="btn btn-danger" onClick={handleRemove}>Удалить</button></td>
    </tr>
  );
};

export default StudentItem;