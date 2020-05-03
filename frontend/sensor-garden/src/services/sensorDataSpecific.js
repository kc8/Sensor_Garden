import React, {Component } from 'react';
import gql from "graphql-tag"
import { ApolloClient } from "apollo-client";
import { InMemoryCache, DefaultOptions} from "apollo-cache-inmemory";
import { HttpLink } from "apollo-link-http";



const cache = new InMemoryCache();

const link = new HttpLink({
  uri: "https://tomato-sensor.ue.r.appspot.com/"
})

const defaultOptions  = {
    watchQuery: {
      fetchPolicy: 'no-cache',
      errorPolicy: 'ignore',
    },
    query: {
      fetchPolicy: 'no-cache',
      errorPolicy: 'all',
    },
  }

const client = new ApolloClient({
  link,
  cache,
  defaultOptions: defaultOptions
});

const getSensorValues = gql`
    query getSensorValues($sensorId: String!) { 
        measurementsSpecificValues(sensorId: $sensorId) 
    {
        commonName
        measurementFriendly
        measurementPrecise
        sensorId
        unitsOfMeasure
    }
    }`;

class SpecificSensorData extends Component {

    constructor(props) {
        super(props)
        this.state = {
            measurementsSpecificValues: [], 
        }
        
    }

    componentDidMount() { 
        this.getData();
        setInterval(this.getData, 10000);
    }

    // To - Do: Figure out how to handle failure
    getData = () => {
        client.query({
            query: getSensorValues, 
            variables: { 
                    sensorId: this.props.sensorId
            }
        }).then(result => this.setState(result.data)
    )}

    render() {
        return (
            <div>
                <section className="hero">
                    <div className="hero-body">            
                        <div className="tile is-ancestor">
                        <div className="tile is-parent">
                            {
                                this.state.measurementsSpecificValues.map(({commonName, measurementFriendly, unitsOfMeasure}) => (
                                    <article key={commonName} className="tile is-child box"> 
                                        <p className="title">{commonName}</p>
                                        <p className="subtitle">{measurementFriendly} {unitsOfMeasure}</p>
                                    </article> 
                                ))
                            }
                        </div>
                        </div>
                    </div>
                </section>
            </div>
                
        )
    }
}


export default SpecificSensorData;