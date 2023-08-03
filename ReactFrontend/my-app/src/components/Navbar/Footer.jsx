import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

function Footer() {
  

  return (
    <div>
    <Card>
      <Card.Header>Footer</Card.Header>
      <Card.Body>
        <Card.Title>Special title treatment</Card.Title>
        <Card.Text>
          With supporting text below as a natural lead-in to additional content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
      <Card.Footer className="text-muted">Current Time is: </Card.Footer>
    </Card>
        <button type="button" className="btn btn-secondary btn-floating mx-1">
        <i className="fab fa-facebook-f" />
      </button>
  
      <button type="button" className="btn btn-secondary btn-floating mx-1">
        <i className="fab fa-google" />
      </button>
  
      <button type="button" className="btn btn-secondary btn-floating mx-1">
        <i className="fab fa-twitter" />
      </button>
  
      <button type="button" className="btn btn-secondary btn-floating mx-1">
        <i className="fab fa-github" />
      </button>
    </div>
  );
}

export default Footer;