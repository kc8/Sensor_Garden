use yew::prelude::*;
use yew_router::prelude::*;

mod components;
use crate::components::{AboutPage, Footer, Header, SensorData, SensorGroup};

#[derive(Copy, Debug, Clone, Routable, PartialEq)]
enum Route {
    #[at("/about")]
    About,
    #[at("/")]
    Home,
    #[at("/data")]
    Data, 
    #[at("/404")]
    NotFound
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
        sensor_data.push( SensorData {
            common_name: sensor.to_string(),
            measurment_friendly: "0.0".to_string(),
            unit_of_measure: "NOTHING".to_string()
        });
    }
    html!{ <SensorGroup sensor_data={sensor_data} />}
}


fn route(routes: Route) -> Html {
    match routes {
        Route::Home => html! {setupDataComp()},
        Route::About => html! {<AboutPage />},
        Route::Data => setupDataComp(),
        Route::NotFound => html! {<h1>{"Not Found"}</h1>},
    }
}

fn main() {
    yew::Renderer::<App>::new().render();
}
