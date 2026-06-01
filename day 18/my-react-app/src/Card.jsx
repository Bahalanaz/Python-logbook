import dog from './assets/dog.jpg'
function Card(){
    return(
        <div className="Card">
            <img className = "Card-image" src = {dog} alt="profile picture"></img>
            <h2 className='Card-title'>Sheesh</h2>
            <p className='Card-text'>I am doge how are ya?</p>
        </div>
    );
}
export default Card