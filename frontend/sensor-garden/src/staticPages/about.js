import React from 'react';


function About() { 

    return (
        <div> 
            <h1>About</h1>
            <article>
                <p>This site displays the sensor readings collected from the garden in the picture below</p>
                <p>Picture to come! We will be re-desining part of the garden in the coming weeks</p>
                <h2>What does each sensor mean</h2>
                <table>
                    <tr>
                        <td>Soil Moisture</td>
                        <td>
                            A rough estimate about how damp or wet the soil is. We try to keep the soil moisture within a specific range. 
                            The moisture is measured with a probe that measures the resistance between two pieces of copper. We currently do not 
                            have a unit of measure
                        </td>
                    </tr>
                    <tr>
                        <td>Soil Temperature</td>
                        <td>
                            The temperature of the soil is measure at 1 inch deep. We keep track of this to see the difference between the ambient temperature
                        </td>
                    </tr>
                    <tr>
                        <td>Ambient Humidity, Pressure and Temperature</td>
                        <td>
                            These ambient measurements are in regards to the surrounding environment. The measurements are taken in the same sunlight that the garden is experiencing. 
                        </td>
                    </tr>
                </table>
            </article>
        </div>
    )
}


export default About