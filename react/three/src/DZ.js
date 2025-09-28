import React from "react";

class Dz extends React.Component {
    state = {
        length: 100  
    }


    handleLengthChange = (event) => {
        this.setState({
            length: parseInt(event.target.value)
        });
    }

    render() {
        let { length } = this.state;
        
        let squareStyle = {
            width: `${length}px`,
            height: `${length}px`,
            backgroundColor: 'blue',
            marginTop: '20px'
        };

        return(
            <div>
                <p>Выберите размер квадрата:</p>
                <p>{length}px * {length}px</p>
                <div>
                    <input 
                        type="range" 
                        min="10" 
                        max="300" 
                        value={length}
                        onChange={this.handleLengthChange}
                    />
                </div>
                <div style={squareStyle}></div>
            </div>
        )
    }
}

export default Dz;