use yew::prelude::*;
use crate::Route;
use yew_router::prelude::*;

#[derive(Clone, PartialEq, Properties)]
pub struct SensorData {
    pub common_name: String,
    pub measurment_friendly: String,
    pub unit_of_measure: String,
}

#[derive(Clone, PartialEq, Properties)]
pub struct Sensor {
    pub sensor_data: Vec<SensorData>,
}

// components
#[function_component]
pub fn AboutPage() -> Html {
    html! {
        <div class="content">
            <h1 class="title is-1">{"About"}</h1>
            <article>
                <p>{"This site displays the sensor readings collected from the garden in the picture below"}</p>
                <p>{"Picture to come! We will be re-designing part of the garden in the coming weeks"}</p>
                <h2>{"Sensor Descriptions"}</h2>
                <table class="table is-striped">
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
        <div class="wrapper">
            <footer class="footer">
                <div class="content has-text-centered">
                    <strong>{"By Kyle Cooper"}</strong>{". View the source code on"}
                    <a href="https://github.com/kc8/Sensor_Garden">{"Github"}</a>{"."}
                </div>
            </footer>
        </div>
    }
}

//TODO loving the clone....
fn create_sesnor_data(props: &Sensor) -> Html {
    // TODO key... for each article that is generated?
    html! {
    { for props.sensor_data.clone().into_iter().map(|s| html_nested! {
            <article class="tile is-child box">
                <p class="title">{s.common_name}</p>
                <p class="subtitle">{s.measurment_friendly} {s.unit_of_measure}</p>
            </article> }) }
    }
}

#[function_component]
fn DataContainer(props: &Sensor) -> Html {
    html! {
        <section class="hero">
            <div class="hero-body">
                <div class="tile is-ancestor">
                    <div class="tile is-parent">
                    { create_sesnor_data(props) }
                    </div>
                </div>
            </div>
        </section>
    }
}

#[function_component]
pub fn SensorGroup(sensor_data: &Sensor) -> Html {
    html! {
        <section class="hero">
          <div class="hero-body">
            <div class="tile is-ancestor">
              <div class="tile is-parent">
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
            if (loading) return <article class="tile is-child box"><p>Loading...</p></article>;
            if (error) return <article class="tile is-child box"><p>Error While Getting Sensor Values for {sensorId}</p></article>;

            return (
                data.measurementsSpecificValues.map(({commonName, measurementFriendly, unitsOfMeasure}) => (
                    <article key={commonName} class="tile is-child box">
                        <p class="title">{commonName}</p>
                        <p class="subtitle">{measurementFriendly} {unitsOfMeasure}</p>
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
          <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
          <div id="navbar" class="navbar-menu">
            <div class="navbar-start">
            <Link<Route> classes="navbar-item is-size-4" to={Route::Home}>{"Home"}</Link<Route>>
            <Link<Route> classes="navbar-item is-size-4" to={Route::About}>{"About"}</Link<Route>>
            <Link<Route> classes="navbar-item is-size-4" to={Route::Home}>{"Live Data"}</Link<Route>>
            </div>
            <div class="navbar-end">
              <div class="navbar-item">
                <div class="buttons">
                </div>
              </div>
            </div>
          </div>
        </nav>
        <section class="hero is-primary">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">{"Sensor Garden"}</h1>
            <h2 class="subtitle">
            </h2>
          </div>
        </div>
    </section>
    </div>
    }
}
