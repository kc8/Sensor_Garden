use gloo_net::http::Request;
use serde::Deserialize;
use yew::prelude::*;
use yew_router::prelude::*;

mod components;
use crate::components::{AboutPage, Footer, Header, SensorData, SensorGroup};

const BACKEND_END_POINT: &str = "https://sgb.cooperkyle.com/getSensorData";
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
        //"soil_temp_plant_2", // I think this is currently broken
    ];
    let data = use_state(|| vec![]);
    {
        let data = data.clone();
        use_effect_with_deps(
            move |_| {
                let data = data.clone();
                wasm_bindgen_futures::spawn_local(async move {
                    let mut final_result: Vec<SensorData> = Vec::new();
                    for sensor in sensor_list {
                        let params = [("sensorId", sensor)];
                        let fss: RawSensorData = Request::get(BACKEND_END_POINT)
                            .query(params)
                            .header(HEADER_AUTH, HEADER_AUTH_VALUE)
                            .send()
                            .await
                            .unwrap()
                            .json()
                            .await
                            .unwrap();
                        final_result.push(SensorData {
                            common_name: fss.SensorName,
                            measurment_friendly: fss.Measurment.to_string(),
                            unit_of_measure: fss.Unit.to_string(),
                        });
                    }
                    data.set(final_result);
                });
                || ()
            },
            (),
        );
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
