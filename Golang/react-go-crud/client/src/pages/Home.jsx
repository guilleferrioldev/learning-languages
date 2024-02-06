import { Container, Row, Col} from 'react-bootstrap'
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Spinner from 'react-bootstrap/Spinner'
import axios from 'axios';

const Home = () => {
    const [apiData, setApiData] = useState(false);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      const fetchData = async () => {
        try {
          const apiURL = "http://localhost:8000/";
          const response = await axios.get(apiURL);

          if (response.status === 200 & response?.data.statusText === "OK") {
            setApiData(response?.data?.blog_records)
          }

          setLoading(false);

        } catch (error) {
          setLoading(false);
          console.log(error.response)
        }
        
      };
      fetchData();
      return () => {};
    }, []);

    if (loading) {
      return (
        <>
          <Container className="spinner">
            <Spinner animation="grow" />
          </Container>
        </>
      )
    }
    
    return (
      <Container className="py-2">
        <Row>
          {apiData && apiData.map((record, index) => (
              <Col key={index} xs="4" className='py-5 box'>
                <div className='title'>
                  <Link to={`/blog/${record.id}`}>{record.title}</Link>
                  </div>
                <div>{record.post}</div>
              </Col>
            ))}
        </Row>
      </Container>
    );
  }

export default Home