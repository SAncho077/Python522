import './article.css'

function Article(props) {
    let { db } = props;
    
    return (
        <div className="content-cards">
            {Object.keys(db).map(key => {
                let movie = db[key];
                return (
                    <a href={`/movie/${movie.index}`} key={movie.index} className="content-cards__item">
                        <div className="content-cards__item--img">
                            <img src={movie.src} alt={movie.title} />
                        </div>
                        <div className="content-cards__item--title">
                            <h5>{movie.title}</h5>
                        </div>
                        <p className="content-cards__item--description">
                            {movie.description}
                        </p>
                        <p className="content-cards__item--rating">
                            Рейтинг: {movie.rating}/10
                        </p>
                    </a>               
                )
            })}
        </div>
    )
}

export default Article;