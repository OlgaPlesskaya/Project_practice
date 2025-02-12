import { useState } from 'react'
import { getNextId } from '/workspaces/test/my-app11/src/data.js';
import '/workspaces/test/my-app11/src/App.css'

const AddStudentForm = ({ onAdd }) => {
  const [name, setName] = useState('');
  const [age, setAge] = useState(18);
  const [course, setCourse] = useState('Computer Science');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name || !age || !course) return;
    
    const newStudent = {
      id: getNextId(), // Генерация уникального ID
      name,
      age,
      course
    };
  
    onAdd(newStudent); // Передача нового объекта студента вверх по иерархии
    setName('');
    setAge(18);
    setCourse('Computer Science');
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
        <label htmlFor="studentName" className="form-label">Имя:</label>
        <input
          type="text"
          id="studentName"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="form-control"
        />
      </div>
      <div className="mb-3">
        <label htmlFor="studentAge" className="form-label">Возраст:</label>
        <input
          type="number"
          id="studentAge"
          value={age}
          onChange={(e) => setAge(parseInt(e.target.value))}
          className="form-control"
        />
      </div>
      <div className="mb-3">
        <label htmlFor="studentCourse" className="form-label">Курс:</label>
        <select
          id="studentCourse"
          value={course}
          onChange={(e) => setCourse(e.target.value)}
          className="form-select"
        >
          <option value="Computer Science">Информатика</option>
          <option value="Mathematics">Математика</option>
          <option value="Physics">Физика</option>
        </select>
      </div>
      <button type="submit" className="btn btn-primary">Добавить студента</button>
    </form>
  );
};

export default AddStudentForm;