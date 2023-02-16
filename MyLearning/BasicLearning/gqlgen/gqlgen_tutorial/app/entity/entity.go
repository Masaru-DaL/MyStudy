package entity

type Company struct {
	ID                    string `json:"id" gqlgen:"id"`
	Name                  string `json:"name" gqlgen:"name"`
	ImageURL              string `json:"image_url" gqlgen:"image_url"`
	Abstract              string `json:"abstract" gqlgen:"abstract"`
	BusinessSummary       string `json:"business_summary" gqlgen:"business_summary"`
	WorkLocation          string `json:"work_location" gqlgen:"work_location"`
	HPURL                 string `json:"hp_url" gqlgen:"hp_url"`
	EmployeeNum           int    `json:"employee_num" gqlgen:"employee_num"`
	Establishment         string `json:"establishment" gqlgen:"establishment"`
	BusinessDetail        string `json:"business_detail" gqlgen:"business_detail"`
	Occupation            string `json:"occupation" gqlgen:"occupation"`
	OccupationDetail      string `json:"occupation_detail" gqlgen:"occupation_detail"`
	SelectionFlow         string `json:"selection_flow" gqlgen:"selection_flow"`
	Comment               string `json:"comment" gqlgen:"comment"`
	EstimatedAnnualIncome int    `json:"estimated_annual_income" gqlgen:"estimated_annual_income"`
	WantedEngineer        string `json:"wanted_engineer" gqlgen:"wanted_engineer"`
	Age                   int    `json:"age" gqlgen:"age"`
	Appeal                string `json:"appeal" gqlgen:"appeal"`
	RequiredSkills        string `json:"required_skills" gqlgen:"required_skills"`
	CareerPlan            string `json:"career_plan" gqlgen:"career_plan"`
}
