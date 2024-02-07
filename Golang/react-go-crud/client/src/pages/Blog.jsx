import { Container, Row, Col} from 'react-bootstrap'
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom'
import axios from 'axios';

const Blog = () =>  {
    const params = useParams();
    const [apiData, setApiData] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
          try {
            const apiURL = "http://localhost:8000/" + params.id;
            const response = await axios.get(apiURL);
  
            if (response.status === 200 & response?.data.statusText === "OK") {
              setApiData(response?.data?.record)
            }
  
          } catch (error) {
            console.log(error.response)
          }
          
        };
        fetchData();
        return () => {};
      }, []);

    console.log(apiData)
    
    return (
        <Container>
            <Row>
                <Col xs="12">
                  <h1>{apiData.title}</h1>
                </Col>
                <Col xs="12">
                  <p>{apiData.post}</p>
                  </Col>
            </Row>
        </Container>
    )
}

export default Blog