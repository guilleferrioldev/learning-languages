import { Container, Row, Col} from 'react-bootstrap'
import { useEffect, useState } from 'react';
import { Link, useLocation  } from 'react-router-dom';
import Spinner from 'react-bootstrap/Spinner'
import axios from 'axios';

const Home = () => {
    const [apiData, setApiData] = useState(false);
    const [loading, setLoading] = useState(true);

    const location = useLocation();

    useEffect(() => {
      const fetchData = async () => {
        try {
          const apiUrl = "http://localhost:8000/";
          const response = await axios.get(apiUrl);

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
          <h3>
            <Link to="add" className="btn btn-primary">
              Add New
            </Link>
          </h3>
          <h5>{location.state && location.state}</h5>
          {apiData && apiData.map((record, index) => (
              <Col key={index} xs="4" className='py-5 box'>
                <div className='title'>
                  <Link to={`/blog/${record.id}`}>{record.title}</Link>
                </div>
                <div>
                <Link to={`edit/${record.id}`}>
                  <i className="fa fa-solid fa-pencil fa-1x" />
                </Link>
                &nbsp;
                <Link to={`delete/${record.id}`}>
                  <i className="fa fa-solid fa-trash fa-1x" />
                </Link>
              </div>
                <div>{record.post}</div>
              </Col>
            ))}
        </Row>
      </Container>
    );
  }

export default Home