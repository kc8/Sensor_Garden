import React, {Component } from 'react';
import gql from "graphql-tag"
import { Query } from 'react-apollo'; 


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

const QueryResults = ({sensorId}) => (
    <Query 
        query={getSensorValues}
        variables={{sensorId}}
        pollInterval = {30000}
        > 
        {({loading, error, data}) => {
            if (loading) return <article className="tile is-child box"><p>Loading...</p></article>; 
            if (error) return <article className="tile is-child box"><p>Error While Getting Sensor Values for {sensorId}</p></article>; 

            return (
                data.measurementsSpecificValues.map(({commonName, measurementFriendly, unitsOfMeasure}) => (
                    <article key={commonName} className="tile is-child box"> 
                        <p className="title">{commonName}</p>
                        <p className="subtitle">{measurementFriendly} {unitsOfMeasure}</p>
                    </article> 
                ))
            )
        }
    }
    </Query>
)

class GetSensorData extends Component {
    render() {
        return (
            <div>
                <section className="hero">
                    <div className="hero-body">            
                        <div className="tile is-ancestor">
                            <div className="tile is-parent">
                                <QueryResults sensorId={this.props.sensorId} /> 
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        )

    }
}


export default GetSensorData;