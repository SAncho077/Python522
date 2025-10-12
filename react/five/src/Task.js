function Task(props) {
    let { task, doneTask, index, deleteTask, cancelTask } = props
    return (
        <div className="task" style={{ textDecoration: task.done ? "line-through" : "" }}>
            {task.text}
            <div>
                <button onClick={() => { doneTask(index) }}>Done</button>
                <button onClick={() => {cancelTask(index)}} >cancel
                </button>
                <button onClick={() => {deleteTask(index)}}>X</button>

            </div>
        </div>
    )
}

export default Task