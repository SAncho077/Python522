import './App.css';
import React from 'react';
// import Hello from './Hello';
// import Length from './Length';
// import Form from './Form';
// import Range from './Range';
import Posts from './Posts';
import Dz from './DZ';


class App extends React.Component {

state = {
    posts: [
      {id: '1', name: "JS Basics", title: "Обучение базовым конструкциям JavaScript"},
      {id: '2', name: "JS Advanced", title: "Обучение расширенным возможностям JavaScript"},
      {id: '3', name: "React JS", title: "Обучение React JS"},
    ]
  }

  removePost = (id) => {
    this.setState({posts: this.state.posts.filter(post => post.id !== id)})
  }


  render() {
    let {posts} = this.state
  return (
    <div>
      <Posts posts={posts} removePost={this.removePost}/>
      {/* <Hello />
      <Length />
      <Form />
      <Range /> */}
      <Dz/>

    </div>
  );
}
}

export default App;
