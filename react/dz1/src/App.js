
import './App.css';
import Header from './Header/header'
import Nav from "./Nav/nav"
import Article from './Article/article';

function App(props) {
  let {nav, db, name} = props
  return (
    <div className="App">
      <Header nav={nav} db={db} name={name}/>
      <Nav nav={nav}/>
      <Article db={db}/>

    </div>
  );
}

export default App;
