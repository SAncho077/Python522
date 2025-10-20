import { useState } from "react";

function Home() {
    const [items, setItems] = useState([
        { name: "Apple", checked: false },
        { name: "Banana", checked: false },
        { name: "Tea", checked: false },
        { name: "Coffee", checked: false }
    ]);

    const toggleItem = (index) => {
        setItems(prevItems => 
            prevItems.map((item, i) => 
                i === index ? { ...item, checked: !item.checked } : item
            )
        );
    }
        const completedCount = items.filter(item => item.checked).length;

    return (
        <div>
            <h2>Home Page</h2>
            <h4 className="shp">Shopping list</h4>
            <div>
                <ul className="list">
                    {items.map((item, index) => (
                        <li key={index}>
                            <input 
                                type="checkbox" 
                                checked={item.checked}
                                onChange={() => toggleItem(index)} 
                            />
                            {item.name} 
                            <button onClick={() => toggleItem(index)}>{item.checked ? '+' : '-'}</button>
                        </li>
                    ))}
                </ul>
                <hr />
            </div>
            
            <h3>Total completed : {completedCount}</h3>
            
        </div>
        
        
    );
}


export default Home