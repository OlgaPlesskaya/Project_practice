import { useState } from 'react'
import './App.css'
import AddStudentForm from '/workspaces/test/my-app11/src/components/AddStudentForm.jsx';
import StudentList from '/workspaces/test/my-app11/src/components/StudentList.jsx';

const App = () => {
  return (
    <div className="container mt-5">
      <h1>Управление студентами</h1>
      <hr />
      <AddStudentForm />
      <StudentList />
    </div>
  );
};

export default App;
