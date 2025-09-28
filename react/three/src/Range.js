import React from "react";

class Range extends React.Component{
    state = {val: 100}

    range = (event) => {
        this.setState({val: event.target.value})
    }

    render(){
        return(
            <>
                <hr />
                <input type="range" onChange={this.range} max="200" min="0" step="10"/>
                <p>{this.state.val}</p>
            </>
        )
    }
}


export default Range