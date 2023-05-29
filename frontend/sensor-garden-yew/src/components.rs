use yew::prelude::*;

// structures

#[derive(Clone, PartialEq, Properties)]
pub struct SensorData {
    common_name: String,
    measurment_friendly: String,
    unit_of_measure: String,
}

#[derive(Clone, PartialEq, Properties)]
pub struct Sensor {
    sensor_data: Vec<SensorData>,
}

// components
#[function_component]
pub fn AboutPage() -> Html {
    html! {
        <div className="content">
            <h1 className="title is-1">{"About"}</h1>
            <article>
                <p>{"This site displays the sensor readings collected from the garden in the picture below"}</p>
                <p>{"Picture to come! We will be re-designing part of the garden in the coming weeks"}</p>
                <h2>{"Sensor Descriptions"}</h2>
                <table className="table is-striped">
                <thead>
                    <tr><td>{"Sensor Name"}</td><td>{"Description"}</td></tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{"Soil Moisture"}</td>
                        <td>
                        {"A rough estimate about how damp or wet the soil. The percent saturation indicates how much water the soil is holding. We try to keep the soil moisture within a specific range.
                            The moisture is measured with a probe that measures the resistance between two pieces of copper. Were 100% means there is no voltage loss and 0% means there is no voltage."}
                        </td>
                    </tr>
                    <tr>
                        <td>{"Soil Temperature"}</td>
                        <td>
                        {"The temperature of the soil is measure at 1 inch deep. We keep track of this to see the difference between the ambient temperature"}
                        </td>
                    </tr>
                    <tr>
                        <td>{"Ambient Humidity, Pressure and Temperature"}</td>
                        <td>
                            {"These ambient measurements are in regards to the surrounding environment. The measurements are taken in the same sunlight that the garden is experiencing."}
                        </td>
                    </tr>
                    </tbody>
                </table>
            </article>
        </div>
    }
}

#[function_component]
pub fn Footer() -> Html {
    html! {
        <div className="wrapper">
            <footer className="footer">
                <div className="content has-text-centered">
                    <strong>{"By Kyle Cooper"}</strong>{". View the source code on"}
                    <a href="https://github.com/kc8/Sensor_Garden">{"Github"}</a>{"."}
                </div>
            </footer>
        </div>
    }
}

//TODO loving the clone....
fn creaete_sesnor_data(props: &Sensor) -> Html {
    // TODO key... for each article that is generated?
    html! {
    { for props.sensor_data.clone().into_iter().map(|s| html_nested! {
            <article className="tile is-child box">
                <p className="title">{s.common_name}</p>
                <p className="subtitle">{s.measurment_friendly} {s.unit_of_measure}</p>
            </article> }) }
    }
}

#[function_component]
fn DataContainer(props: &Sensor) -> Html {
    html! {
        <section className="hero">
            <div className="hero-body">
                <div className="tile is-ancestor">
                    <div className="tile is-parent">
                    { creaete_sesnor_data(props) }
                    </div>
                </div>
            </div>
        </section>
    }
}

#[function_component]
pub fn SensorGroup(sensor_data: &Sensor) -> Html {
    html! {
        <section className="hero">
          <div className="hero-body">
            <div className="tile is-ancestor">
              <div className="tile is-parent">
              <DataContainer ..sensor_data.clone() />
              </div>
            </div>
          </div>
        </section>
    }
}

#[function_component]
// TODO
pub fn QuerySensor() -> Html {
    html! {
        <></>
    }
    /*
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
    </Query>*/
}

#[function_component]
pub fn Header() -> Html {
    html! {
    <div>
          <nav className="navbar is-primary" role="navigation" aria-label="main navigation">
          <div id="navbar" className="navbar-menu">
            <div className="navbar-start">
            <a className="navbar-item is-size-4" to="/">{"Home"}</a>
            <a className="navbar-item is-size-4" to="/about">{"About"}</a>
            <a className="navbar-item is-size-4" to="/">{"Live Data"}</a>
            </div>
            <div className="navbar-end">
              <div className="navbar-item">
                <div className="buttons">
                </div>
              </div>
            </div>
          </div>
        </nav>
        <section className="hero is-primary">
        <div className="hero-body">
          <div className="container">
            <h1 className="title">{"Sensor Garden"}</h1>
            <h2 className="subtitle">
            </h2>
          </div>
        </div>
    </section>
    </div>
    }
}
