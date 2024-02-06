import { Container, Row, Col} from 'react-bootstrap'
import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css'

function App () {
  const [apiData, setApiData] = useState(false);

    useEffect(() => {
      const fetchData = async () => {
        try {
          const apiURL = "http://localhost:8000";
          const response = await axios.get(apiURL);

          if (response.status === 200 & response?.data.statusText === "OK") {
            setApiData(response?.data?.blog_records)
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
          <Col xs="12" className="py-2">
            <h1 className="text-center">
              React Application with Go Fiber Backend
            </h1>
          </Col>

          {apiData && apiData.map((record, index) => (
              <Col key={index} xs="4" className='py-5 box'>
                <div className='title'>{record.title}</div>
                <div>{record.post}</div>
              </Col>
            ))}
        </Row>
      </Container>
    );
  }
  
export default App