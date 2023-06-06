use gloo_net::http::Request;
use serde::Deserialize;
use serde_json::json;
use yew::prelude::*;
use yew_router::prelude::*;

mod components;
use crate::components::{AboutPage, Footer, Header, SensorData, SensorGroup};

// const BACKEND_END_POINT: &str = "https://sgb.cooperkyle.com/getSensorData";
const BACKEND_END_POINT: &str = "http://127.0.0.1:8085/getSensorData";
const HEADER_AUTH: &str = "AUTH-HEADER";
const HEADER_AUTH_VALUE: &str = "temp value";

#[derive(Copy, Debug, Clone, Routable, PartialEq)]
enum Route {
    #[at("/about")]
    About,
    #[at("/")]
    Home,
    #[at("/data")]
    Data,
    #[at("/404")]
    NotFound,
}

#[derive(Clone, PartialEq, Deserialize)]
pub struct RawSensorData {
    pub SensorName: String,
    pub Id: String,
    pub Status: String,
    pub Unit: String,
    pub Measurment: f32,
}

#[function_component]
fn RequestSensorData() -> Html {
    let sensor_list = vec![
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "ambient_humidity",
        "ambient_temp",
        "ambient_pressure",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
    ];
    let sens_name_copy = sensor_list[0].to_string();
    /*let data = use_state(|| vec![SensorData {
        common_name: "TEST".to_string(),
        measurment_friendly: "1.0".to_string(),
        unit_of_measure: "".to_string()
    }]);*/
    let data = use_state(|| vec![]);
    {
        let data = data.clone();
        use_effect_with_deps(move |_| {
            let data = data.clone();
                wasm_bindgen_futures::spawn_local(async move {
                    let params = [("sensorName", sens_name_copy)];
                    let fss: RawSensorData = Request::get(BACKEND_END_POINT)
                        .query(params)
                        .header(HEADER_AUTH, HEADER_AUTH_VALUE)
                        .send()
                        .await
                        .unwrap()
                        .json()
                        .await
                        .unwrap();
                    data.set(vec![ 
                               SensorData {
                        common_name: fss.SensorName,
                        measurment_friendly: fss.Measurment.to_string(),
                        unit_of_measure: fss.Unit.to_string()
                    }]);
                });
                || ()
            }, ());
    }
    html! { <SensorGroup sensor_data={(*data).clone()}/>}
}

#[function_component(App)]
fn app() -> Html {
    html! {
        <BrowserRouter>
            <div class="site">
                <Header />
                <main class="site-content">
                    <Switch<Route> render={route} />
                </main>
                <Footer />
            </div>
        </BrowserRouter>
    }
}

fn setupDataComp() -> Html {
    let sensor_list = vec![
        "soil_moisture_plant_1",
        "soil_moisture_plant_2",
        "ambient_humidity",
        "ambient_temp",
        "ambient_pressure",
        "soil_temp_plant_1",
        "soil_temp_plant_2",
    ];
    let mut sensor_data: Vec<SensorData> = Vec::new();

    for sensor in sensor_list {
        sensor_data.push(SensorData {
            common_name: sensor.to_string(),
            measurment_friendly: "0.0".to_string(),
            unit_of_measure: "NOTHING".to_string(),
        });
    }
    html! { <SensorGroup sensor_data={sensor_data} />}
}

fn route(routes: Route) -> Html {
    match routes {
        Route::Home => html! {<RequestSensorData />},
        Route::About => html! {<AboutPage />},
        Route::Data => html! {<RequestSensorData /> },
        Route::NotFound => html! {<h1>{"Not Found"}</h1>},
    }
}

fn main() {
    yew::Renderer::<App>::new().render();
}
