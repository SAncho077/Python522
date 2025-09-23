import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import db from "./db.json"

let nav = {"Главная": "/index", "Новости": "/news", "О компании": "/about", "Магазин": "/shop", "Контакты": "/contacts"}

let name = "Sanjar"



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App nav = {nav} db = {db} name={name}/>
  </React.StrictMode>
);


