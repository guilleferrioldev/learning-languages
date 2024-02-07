import { useNavigate, useParams } from "react-router-dom";
import { Container, Row, Col } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import axios from 'axios'

const Delete = () => {
    const params = useParams();
    const navigate = useNavigate()

    const handleDelete = async () => {
        try {
            const apiUrl = "http://localhost:8000/" + params.id;
            const response = await axios.delete(apiUrl);
    
            if (response.status === 200) {
                navigate("/", {
                    state: "Record deleted successfully",
                  });
            }
          } catch (error) {
            console.log(error.response);
          }
    }

    return (
        <>
        <Container>
            <Row>
            <h1>Are you sure to delete this record</h1>
                <Col xd="12" className="py-5 d-flex justify-content-around">
                <button className="btn btn-danger py-2" onClick={handleDelete}>
                 Yes
                </button>
                <Link to="/" className="btn btn-secondary">
                 NO
                </Link>
                </Col>
            </Row>
        </Container>
        </>
    )
}

export default Delete